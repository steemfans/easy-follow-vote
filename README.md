# Easy Follow Vote

### How to run

```
docker run -itd --restart always \
    --name follow-vote \
    -e STEEMD=https://api.steem.fans \
    -e WORKER_NUM=1 \
    -e TO_FOLLOW=justyy,wherein \
    -e VOTER=ety001 \
    -e VOTER_PRIV_KEY=5J****** \
    -e WEIGHT=50 \
    -e VP_THRESHOLD=30 \
    steemfans/easy-follow-vote:latest
```

### Issues
If you have any issue, please be easy to submit on the [issue page](https://github.com/steemfans/easy-follow-vote/issues).

### Vote
I'm also a witness. Thank you for [voting me](https://steemlogin.com/sign/account-witness-vote?witness=ety001&approve=1).
