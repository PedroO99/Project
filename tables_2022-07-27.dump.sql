----
-- phpLiteAdmin database dump (https://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.9-dev
-- Exported: 5:15pm on July 27, 2022 (UTC)
-- database file: /workspaces/77199504/project/tables.db
----
BEGIN TRANSACTION;

----
-- Table structure for users
----
CREATE TABLE users (user_id INTEGER, name TEXT NOT NULL, password TEXT NOT NULL, sexo TEXT NOT NULL, email TEST NOT NULL, PRIMARY KEY(user_id));

----
-- Data dump for users, a total of 7 rows
----
INSERT INTO "users" ("user_id","name","password","sexo","email") VALUES ('1','Pedro Oviedo','pbkdf2:sha256:150000$Sk1bCL07$e5151aa0f7df95c31bfd33c554e1bae93bcc88459124473949aa93954280d5a4','M','pe@g.com');
INSERT INTO "users" ("user_id","name","password","sexo","email") VALUES ('2','Pedro Marcelo Oviedo','pbkdf2:sha256:150000$6xUG5xWA$977ce69840a0dacc6163f49e839917359a7111ce9145a626057c5f1d691f4653','M','pmo@g.com');
INSERT INTO "users" ("user_id","name","password","sexo","email") VALUES ('3','Lorenzo Gui','pbkdf2:sha256:260000$eS0xWoWGxivIPCBe$a6bb8c5b71cabe275c01d18f6f2aa6497b1acc6054b1b8c6ef0ba32b1aa166e4','M','ljg@g.com');
INSERT INTO "users" ("user_id","name","password","sexo","email") VALUES ('4','Manuela Oviedo','pbkdf2:sha256:260000$EC2smOcLWZyuApET$0021d061cd445b5d9cec1dee987e84b279a04bd5b6c33908a8005319c4130630','F','manu@g.com');
INSERT INTO "users" ("user_id","name","password","sexo","email") VALUES ('5','Maria Paula Galella','pbkdf2:sha256:260000$qPYMvzeVViQdyKa1$b0c463e5fcbda8645b8d192d6f1b00e8f6db0b24031f164eee54c46420afd4f5','F','mama@g.com');
INSERT INTO "users" ("user_id","name","password","sexo","email") VALUES ('6','Tomas Becher','pbkdf2:sha256:260000$uc8kudwh36LDDu3L$bccab2d1b8f35636d2d7011e453c2291214f34ba3808f0d2dd579d420077ed9f','M','becher@g.com');
INSERT INTO "users" ("user_id","name","password","sexo","email") VALUES ('7','Jesus Gimenez','pbkdf2:sha256:260000$oHG2HhlWbXqo9LIP$336d0f5fbde77905863a8fd2abc9f849b3cf79e39f0356c826ac5b6af47289b8','M','kechu@g.com');

----
-- Table structure for game
----
CREATE TABLE game (user_id INTEGER, rival_id INTEGER, month INTEGER, day INTEGER, hour STRING, winner_id INTEGER, status TEXT NOT NULL DEFAULT Waiting, FOREIGN KEY (user_id) REFERENCES users(user_id));

----
-- Data dump for game, a total of 59 rows
----
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','5','9','18:37','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','3','5','16','14:29','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','1','5','16','14:31','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','3','5','22','15:32','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','2','5','19','15:02','3','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','6','10','10:24','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','1','6','9','10:53','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','1','6','10','18:04','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','5','13:08','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','3','7','5','13:14','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','3','7','5','13:19',NULL,'Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','3','7','5','13:20','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','5','14:21','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','5','13:57','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','1','7','5','14:04','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','1','7','5','14:48','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','6','10:04','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','2','7','6','16:51','3','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','3','7','6','15:56','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','3','7','6','15:59','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','2','7','7','16:04','3','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','1','7','6','16:05','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','3','7','6','16:06','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','2','7','6','16:10','3','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','1','7','6','16:18','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','6','16:23','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','1','7','7','09:22','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','3','7','7','09:29','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','7','09:30','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','3','7','7','09:35','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','7','09:43','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','3','7','7','12:33','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','3','7','8','09:58','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','2','7','8','10:03','3','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','2','7','8','11:39','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('5','4','7','8','10:45','5','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('2','1','7','20','13:40','2','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('3','2','7','20','13:47','3','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('5','4','7','21','14:10','5','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('4','4','7','20','14:15',NULL,'Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('4','5','7','21','14:15','4','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('5','4','7','20','14:18','5','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','3','7','21','14:19','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','6','7','21','14:37','6','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('1','3','7','21','14:52','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('7','2','7','20','14:54','2','Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','7','7','25','16:25','7','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','2','7','27','16:33','2','Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','2','7','26','17:09','2','Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','2','7','27','23:32','2','Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('7','2','7','26','23:39',NULL,'Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('7','3','7','26','23:40','7','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('7','1','7','26','23:46','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','2','7','26','23:47',NULL,'Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','2','7','26','23:49',NULL,'Declined');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('7','1','7','26','23:52','1','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','1','7','27','14:41','6','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','1','7','27','14:42','6','Finished');
INSERT INTO "game" ("user_id","rival_id","month","day","hour","winner_id","status") VALUES ('6','1','7','27','14:45','6','Finished');

----
-- Table structure for ranking
----
CREATE TABLE ranking (user_id INTEGER, sexo TEXT NOT NULL, ranking INTEGER DEFAULT 1200, FOREIGN KEY (user_id) REFERENCES users (user_id));

----
-- Data dump for ranking, a total of 7 rows
----
INSERT INTO "ranking" ("user_id","sexo","ranking") VALUES ('1','M','1199.712185288');
INSERT INTO "ranking" ("user_id","sexo","ranking") VALUES ('2','M','1279.3668137369');
INSERT INTO "ranking" ("user_id","sexo","ranking") VALUES ('3','M','1160.0575644684');
INSERT INTO "ranking" ("user_id","sexo","ranking") VALUES ('4','F','1200');
INSERT INTO "ranking" ("user_id","sexo","ranking") VALUES ('5','F','1200');
INSERT INTO "ranking" ("user_id","sexo","ranking") VALUES ('6','M','1160.8634374605');
INSERT INTO "ranking" ("user_id","sexo","ranking") VALUES ('7','M','1199.9999990463');
COMMIT;
