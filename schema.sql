DROP TABLE IF EXISTS games;
CREATE TABLE games (
  id integer primary key autoincrement,
  name string not null,
  rating integer not null,
  date_released date, not null
);
