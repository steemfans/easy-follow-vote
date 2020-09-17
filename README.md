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

* `STEEMD` is the api url.
* `WORKER_NUM` is the total of worker.
* `TO_FOLLOW` is the people you want to follow voting.
* `VOTER` is the username who vote.
* `VOTER_PRIV_KEY` is the posting key of `VOTER`.
* `WEIGHT` is the vote weight. It need be bigger than 0 and lower than 100. The unit is %.
* `VP_THRESHOLD` is the threshold of voting power. The default value is 30%. The unit is %.

### Issues
If you have any issue, please be easy to submit on the [issue page](https://github.com/steemfans/easy-follow-vote/issues).

### Vote
I'm also a witness. Thank you for [voting me](https://steemlogin.com/sign/account-witness-vote?witness=ety001&approve=1).
