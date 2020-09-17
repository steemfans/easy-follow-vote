# Easy Follow Vote

### How to run

```
docker run -itd --restart always \
    --name follow-vote \
    -e STEEMD=https://api.steem.fans \
    -e WORKER_NUM=1 \
    -e TO_FOLLOW=justyy,wherein \
    -e VOTER=ety001 \
    -e WEIGHT=5000 \
    -e VOTER_PRIV_KEY=5J****** \
    steemfans/easy-follow-vote
```
