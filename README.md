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
    -e WEIGHT_THRESHOLD=30 \
    steemfans/easy-follow-vote
```
