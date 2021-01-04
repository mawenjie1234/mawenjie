
# 重构版本ES日志
## picture_enter 同flurry picture_enter 一致
* pic_name 
* source
* is_reward
* complete_percentage
* picStatus
## picture_ababdon 按了返回键退出切图没有完成
* pic_name
* source
* picStatus
* isReward
* complete_percentage

## picture_complete 图片完成
* pic_name
* source
* picStatus
* isReward : 0, 1

## drawing_background 绘画页面退到后台
* pic_name
* source
* picStatus
* isReward : 0, 1
* complete_percentage

## Fullscreen_ad_did_show 全屏广告展示出来后
* Source : ad source, 和flurry 中广告展示的source 一样。比如 enter
* Interstitial_id 广告的id。

## app_launch app 启动
* first_login_time 用户生命周期首次登入时间

## page_show 界面展示
* ui
  1. SPLASH
  2. HOME
  3. CATEGORY_ALL_PIC
  4. MY_ART
  5. DRAWING
  6. COMPLETE
  7. SHARE
  
## click 点击事件
* click
  1. home_carousel
  2. home_watch_video
  3. home_watch_video_try_again
  4. category_reward_try_again
  5. category_watch_video
  6. myart
  7. categories
  8. complete
  9. share_cancel
  10. share_save
  11. share_insragram
  12. share_other
  13. home_reward
  14. category_reward


## 参数说明
* source 和flurry的相同
* picStatus 如下取值
  1. NOT_START
  2. START
  3. PAINTING
  4. FINISHED