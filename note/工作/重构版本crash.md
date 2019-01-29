1 textureVideo 从使用以来一直崩溃，如果gif可以的话，可以使用gif。毕竟熟悉。
2 应该 修复 weak Notification ，避免内存泄漏。新的crash有5个是 oom。
3 see more 界面 category 为空。场景发送在Main Activity 的onStart(),因该是恢复的时候。
    有可能的原因： 应该是和之前一样数据层没有准备好，获取的时候返回了空.
4 RewardDialog 在AcbUtnity 视频没有看完回调回来后，getView()是空，
  应该是回调回来的时候，dialog 还没有重建。应该添加空保护。不过添加空保护后，ui应该会错乱，比如这个时候应该按钮变成
  tryAgain, 或者直接关闭整个dialog。看做了空保护后应该怎么操作。