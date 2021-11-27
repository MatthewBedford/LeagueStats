DROP TABLE IF EXISTS champions;

CREATE TABLE champions (
    champID     TEXT PRIMARY KEY,
    champName   TEXT NOT NULL,
    icon        TEXT NOT NULL
);