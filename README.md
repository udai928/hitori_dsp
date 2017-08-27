# hitori_dsp

## mysql by docker

 ```
 docker run --name mysql_for_hitoriDSP -e MYSQL_ROOT_PASSWORD=root -d -p 33333:3306 mysql
 mysql -uroot -h 0.0.0.0 --port 33333 -p
 ```



## ad_campaign

* ad_campaign has more than 1 creative.
* ad_campaign has GoalCPA( or GoalCPC)
* ad_campaign has targeting? bid algorythim?
* ad_campaign has 1 budget.


## creative

* creative has 1 image url.
* creative has 1 lp url.
* creative has 1 size.(width x height)
* creatiev has 1 category.
*



## relay_ad_campaign_creative

* ad_campaign x creative


##