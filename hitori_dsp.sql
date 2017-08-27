
DROP DATABASE IF EXISTS hitori_db;
CREATE DATABASE hitori_db;

-- show create table ad_campaign;

CREATE TABLE `ad_campaign` (
      `ad_campaign_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `ad_campaign_name` varchar(255),
      `budget` decimal(18,8) NOT NULL DEFAULT '0',
      `goal_type` enum('cpa','cpc') NOT NULL DEFAULT 'cpc',
      `goal_value` decimal(9,2) NOT NULL DEFAULT '0.00',
      `soft_delete_flag` enum('open','deleted') NOT NULL DEFAULT 'open',
      `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      `create_time` timestamp NOT NULL DEFAULT '2011-01-01 00:00:00',
      PRIMARY KEY (`ad_campaign_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- show create table creative;

CREATE TABLE `creative` (
	  `creative_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
	  `creative_name` varchar(255),
	  `width` smallint(5) unsigned NOT NULL,
	  `height` smallint(5) unsigned NOT NULL,
	  `image_url` text,
	  `landing_page_url` text,
	  `descriptions` varchar(255),
	  `soft_delete_flag` enum('open','deleted') NOT NULL DEFAULT 'open',
	  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	  `create_time` timestamp NOT NULL DEFAULT '2017-01-01 00:00:00',
	  PRIMARY KEY (`creative_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- show create table relay_ad_campaign_creative;

CREATE TABLE `relay_ad_campaign_creative` (
      `ad_campaign_id` int(10) unsigned NOT NULL ,
      `creative_id` int(10) unsigned NOT NULL,
      `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (`ad_campaign_id`,`creative_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- test data insert.

insert into ad_campaign (ad_campaign_name,budget,goal_value,create_time) values
('レッドリボン軍',1000,100,now())
,('イエローリボン軍',1000,50,now())
,('ピンクリボン軍',1000,10,now());

insert into creative (creative_name,width,height,image_url,landing_page_url,create_time) values
('レッド300x250',300,250,'https://placehold.jp/FF0000/FFFFFF/300x250.png','https://recruit.microad.co.jp/?page_id=56',now())
,('レッド728x90',728,90,'https://placehold.jp/FF0000/FFFFFF/728x90.png','https://recruit.microad.co.jp/?page_id=56',now())
,('レッド320x50',320,50,'https://placehold.jp/FF0000/FFFFFF/320x50.png','https://recruit.microad.co.jp/?page_id=56',now())
,('イエロー300x250',300,250,'https://placehold.jp/FFFF00/FFFFFF/300x250.png','https://recruit.microad.co.jp/?page_id=56',now())
,('イエロー728x90',728,90,'https://placehold.jp/FFFF00/FFFFFF/728x90.png','https://recruit.microad.co.jp/?page_id=56',now())
,('イエロー320x50',320,50,'https://placehold.jp/FFFF00/FFFFFF/320x50.png','https://recruit.microad.co.jp/?page_id=56',now())
,('ピンク300x250',300,250,'https://placehold.jp/FF00FF/FFFFFF/300x250.png','https://recruit.microad.co.jp/?page_id=56',now())
,('ピンク728x90',728,90,'https://placehold.jp/FF00FF/FFFFFF/728x90.png','https://recruit.microad.co.jp/?page_id=56',now())
,('ピンク320x50',320,50,'https://placehold.jp/FF00FF/FFFFFF/320x50.png','https://recruit.microad.co.jp/?page_id=56',now())
;

insert into relay_ad_campaign_creative () values
(1,1)
,(1,2)
,(1,3)
,(2,4)
,(2,5)
,(2,6)
,(3,7)
,(3,8)
,(3,9);