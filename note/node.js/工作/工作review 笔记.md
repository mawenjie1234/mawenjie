precview 按钮自己review：

1. 命名都改成preview color btn ✅
2. mPreviewBtnUpHandler -> mPreviewBtnTouchUpHandler✅
3. mColorPictureBtnZListener 应该是只有开关打开的时候创建对象，不能类初始化的时候就创建✅
4. mColorPictureBtnZListener里面实际上不需要 Action_MOVe，✅
5. 应该有一个方法叫changeAllItemPictureColor(boole colorPicture), 而不是使用  setColorPictureEnable(true);  updateAllPictureItem();✅
6. toast 方法可以直接放到一个Utils钟的方法中，✅
7. PictureAdapter 中的 getItemId 是否有用，因为看起来像是一个没有用的东西，如果有用，需要写清楚注释为啥要这么写。✅


log_es_merge review结果：
1. 需要让 press_button_show_color_picture 合并到dev上，并且 修改 PixelApplication中的setShowingView ❎
2. 应该删除Drawing 的 mPictureID，mCategoryName, 真正确保不会频繁的调用 getPictureMeta方法。
3. recordActivity 中加入es的数据后，导致一个函数变得太大了，必须要拆解开。
4. InterstitialHelper 中，添加的cglog可以写到logDidFlurryEvent 中，并改名
5. CGlog.java 中 判断是否发送成功不正确 ✅
6. CGlog.java init和两个observer 是static 有没有问题。
7. CGlog.java 中log 的参数是jsonObject，但是实际上外接使用时很难受的，因为需要加上try catch， 有没有一种更好的参数类型。
8. CGUserInfo 是否有直接的API可以知道 两个calendar 之间差是多少天，来解决 getDaySinceInstallation 每次需要算，或者监听日子变化等待，用缓存来避免这个函数过多的运算。
9. 当前完成的比例必须再次封装，
10. getUserMediaSource 可以写到CGUserInfo  ✅



es_24 review

PlayerData.getInstance().setNotificationSessionFirst(false);✅
Main setLastClickedPicture 不能用
所有的 position 都恢复原状。 
删除 CategoryAdapter onCreateViewHolder✅
删除 CategoryItemViewHolder 的优化

添加item 点击 logOnPictureClick ：  new_complete, new_blank, new_uncomplete, old

    RecyclerView.RecycledViewPool recycledViewPool = new RecyclerView.RecycledViewPool();


