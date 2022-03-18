DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(15) UNIQUE,
    password VARCHAR(30)
);

INSERT INTO users (username, password) VALUES ('admin','StRoNg.PaSsWoRd123');
INSERT INTO users (username, password) VALUES ('user','ThisIsAPassword123');