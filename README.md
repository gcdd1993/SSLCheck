# SSLCheck
> 批量检测域名SSL证书，并进行通知

# 使用
## 配置
```yaml
domains:
  - www.baidu.com # 待检测域名列表
notify:
  - type: QYWX # 通知类型，QYWX=企业微信机器人
    key: "" # 企业微信机器人Key
    mentioned: # 企业微信@
      name: # 企业微信用户名
        - xxx
      phone: # 企业微信手机号
        - xxx
```

## Docker运行
```bash
docker run --rm -v $PWD/config.yaml:/scripts/config.yaml gcdd1993/ssl-check
```

## DockerCompose运行
创建`docker-compose.yml`
```yaml
version: '3.8'

services:
  ssl-check:
    image: gcdd1993/ssl-check
    container_name: ssl-check
    volumes:
      - ./config.yaml:/scripts/config.yaml
```

然后执行
```bash
docker-compose up
```