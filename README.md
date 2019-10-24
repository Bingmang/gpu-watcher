# gpu-watcher

![mark](http://cdn.iblue.tech/img/20191024/XCGoYOOFxAnG.png?imageslim)

## 依赖

python3

client:
```bash
pip install yaml pynvml
```

server:
```bash
pip install yaml pynvml flask
```

## 使用方式

修改 `config.yaml`

```yaml
lab:
  center:
    ip: 202.204.62.145 // 中心节点的ip和端口（汇总GPU信息用）
    port: 80

local:
  host: G1_4GTX1080Ti // 本机hostname（在看板上的名称）
```

client：

```bash
nohup python ping.py &
```

server:

```bash
nohup python server.py &
```
