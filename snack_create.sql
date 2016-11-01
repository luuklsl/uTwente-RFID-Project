--------------------------------------------------------------------------------;
DROP TABLE IF EXISTS key;
CREATE TABLE key
(
kid INTEGER NOT NULL PRIMARY KEY,     -- key id
keyhash BLOB                          -- sha3_512 hash rfid tag uid; BLOB = Binary Large OBject, maybe TEXT also acceptable?
); 

--------------------------------------------------------------------------------;
DROP TABLE IF EXISTS person;     
CREATE TABLE person                     
(
pid INTEGER NOT NULL PRIMARY KEY,     -- person id
name VARCHAR,
sid INTEGER UNIQUE,                   -- student id
balance DECIMAL (5,2) DEFAULT 0,      -- SHOULD ONLY BE NUMBERS, DO NOT USE THE 'FEATURE' of strings, check this in python/js input!
usertype TINYINT                      -- 0: user, 1: admin

);
--------------------------------------------------------------------------------;
DROP TABLE IF EXISTS KPL;

CREATE TABLE KPL 
(
kid INTEGER NOT NULL,                 -- key id
pid INTEGER NOT NULL,                 -- person id
PRIMARY KEY (kid,pid),
FOREIGN KEY(kid) REFERENCES KEY(kid),
FOREIGN KEY(pid) REFERENCEs person(pid)
);
--------------------------------------------------------------------------------
DROP TABLE IF EXISTS categories;

CREATE TABLE categories
(
cid INTEGER PRIMARY KEY NOT NULL, -- category id
name varchar
);
INSERT INTO categories VALUES(0, 'Drinks');
INSERT INTO categories VALUES(1, 'Food');
--------------------------------------------------------------------------------
DROP TABLE IF EXISTS items;

CREATE TABLE items
(
iid INTEGER PRIMARY KEY NOT NULL,      -- item id
item_name varchar,
stock INTEGER,  --make db constraint that always above > -1?,
current_price DECIMAL(5,2), --is most likely just overkill for a snack system,
pic_url text,
cid INTEGER
CHECK(pic_url <> ''),
FOREIGN KEY(cid) REFERENCES categories(cid)
);
INSERT INTO items VALUES(1,'Bueno',20,0.41,'xx', 1);
--------------------------------------------------------------------------------
DROP TABLE IF EXISTS basket;

CREATE TABLE basket
(
bid INTEGER PRIMARY KEY NOT NULL,     -- basket ID
total DECIMAL(5,2),                   -- never directly accessed by user, should be safe
date datetime,                        -- in YYYY-MM-DD HH-MM-SS format
pid NOT NULL,                         -- person id
FOREIGN KEY(pid) REFERENCES person(pid)
);
INSERT INTO basket VALUES (1,15.62,CURRENT_TIMESTAMP,2);
--------------------------------------------------------------------------------
DROP TABLE IF EXISTS transactions;

Create TABLE transactions
(
bid INTEGER NOT NULL,                 -- basket ID
iid INTEGER NOT NULL,                 -- Item ID
quantity INTEGER,                     -- amount of times this item
price DECIMAL(5,2),                   -- Price as found in system on time of Buying
PRIMARY KEY (bid,iid),
FOREIGN KEY(bid) REFERENCES basket(bid),
FOREIGN KEY (iid) REFERENCES items(iid)
)