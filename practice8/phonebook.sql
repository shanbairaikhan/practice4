DROP TABLE IF EXISTS phonebook;

CREATE TABLE phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(100)
);

CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT c.name, c.phone
        FROM phonebook c
        WHERE c.name ILIKE '%' || p_pattern || '%'
           OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_contacts(names VARCHAR[], phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_data TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\d+$' THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]);
        END IF;
    END LOOP;

    IF array_length(invalid_data, 1) IS NOT NULL THEN
        RAISE NOTICE 'Invalid data: %', array_to_string(invalid_data, ',');
    END IF;
END;
$$;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM phonebook
        ORDER BY id
        LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_contact(p_name VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    ELSE
        RAISE NOTICE 'No name or phone provided!';
    END IF;
END;
$$;

CALL upsert_contact('Arai', '87771234567');
CALL upsert_contact('Arai2', '87771234568');
CALL upsert_contact('Arai3', '87771234569');
CALL upsert_contact('Arai4', '87771234560');

SELECT * FROM search_contacts('8777');

SELECT * FROM get_contacts_paginated(2, 0);

CALL insert_many_contacts(ARRAY['John', 'Jane'], ARRAY['123456', '654321']);

SELECT * FROM phonebook;

CALL delete_contact(p_name := 'Arai3');

SELECT * FROM phonebook;