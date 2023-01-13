-- creates the messages table with an id, content and created_at columns.
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content VARCHAR(280) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- creates the likes table with an id, message_id and created_at columns. The message_id column references the id column of the messages table and is set to CASCADE on delete.

CREATE TABLE likes (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages(id) ON DELETE CASCADE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
-- creates a trigger function update_likes_count() which update the messages table, incrementing the likes_count column by 1 when a new like is added and decrementing it by 1 when a like is removed.
CREATE OR REPLACE FUNCTION update_likes_count()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        UPDATE messages SET likes_count = likes_count + 1 WHERE id = NEW.message_id;
    ELSIF (TG_OP = 'DELETE') THEN
        UPDATE messages SET likes_count = likes_count - 1 WHERE id = OLD.message_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
-- creates a trigger update_likes_count_trigger that is called after any insertion or deletion made on the likes table and executes the update_likes_count() function.

CREATE TRIGGER update_likes_count_trigger
AFTER INSERT OR DELETE ON likes
FOR EACH ROW
EXECUTE FUNCTION update_likes_count();
