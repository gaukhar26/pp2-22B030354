import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="пфглрфктгкпфшырф2607",
    database="postgres"
)
cur = conn.cursor()

Q1 = """
    CREATE OR REPLACE FUNCTION search_by_pattern(pattern text)
    RETURNS SETOF Phonebook AS $$
    DECLARE
        result_row Phonebook%ROWTYPE;
    BEGIN
        FOR result_row IN SELECT * FROM Phonebook WHERE name ILIKE '%' || pattern || '%' OR CAST(number AS TEXT) LIKE '%' || pattern || '%' LOOP
            RETURN NEXT result_row;
        END LOOP;
        RETURN;
    END;
    $$ LANGUAGE plpgsql

"""
# cur.execute(Q1)
# cur.execute("SELECT * FROM search_by_pattern('1')")
# for x in cur:
#     print(x)

Q2 = """
    CREATE OR REPLACE PROCEDURE insert_data(IN v_name text, v_number integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        IF EXISTS(SELECT * FROM Phonebook WHERE name = v_name) THEN
            UPDATE Phonebook SET number = v_number WHERE name = v_name;
        ELSE
            INSERT INTO Phonebook (name, number) VALUES (v_name, v_number);
        END IF;
    END;
    $$;
"""
# cur.execute(Q2)
# cur.execute("CALL insert_data(%s, %s)", ("erlen", 9999))
# conn.commit()

Q3 = """
    CREATE PROCEDURE delete_by_pattern(IN pattern text)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM Phonebook WHERE name = pattern OR CAST(number as text) = pattern;
    END;
    $$ 
"""
# cur.execute(Q3)
# cur.execute("CALL delete_by_pattern('dasha')")
# conn.commit()


Q4 = """
    CREATE OR REPLACE PROCEDURE insert_many_users(IN names TEXT[], IN numbers INT[], OUT invalid TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE 
    i INTEGER;
    existing_numbers INT[];
BEGIN
    invalid := ARRAY[]::TEXT[];
    FOR i IN 1..array_length(names, 1) LOOP
        IF EXISTS(SELECT * FROM Phonebook WHERE number = numbers[i]) THEN
            invalid := array_append(invalid, names[i]);
        ELSE
            INSERT INTO Phonebook (name, number) VALUES (names[i], numbers[i]);
        END IF;
    END LOOP;
END;
$$;
"""

# cur.execute(Q4)
# names = ['ddd', 'erlen']
# numbers = [555, 9999]
#
# invalid_data = []
# cur.execute("CALL insert_many_users(%s::TEXT[], %s::INT[], %s)", (names, numbers, invalid_data))
# result = cur.fetchall()
# conn.commit()
# for x in result:
#     print(x, "cannot add")


Q5 = """
    CREATE OR REPLACE FUNCTION query_pagination_func(offset_v integer, limit_v integer)
    RETURNS TABLE (id integer, name varchar, number integer)
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY EXECUTE format('SELECT id, name, number FROM Phonebook ORDER BY id OFFSET %s LIMIT %s', offset_v, limit_v);
    END;
    $$;
"""
# cur.execute(Q5)
# cur.execute("SELECT * FROM query_pagination_func(3, 3)")
# for x in cur:
#     print(x)
