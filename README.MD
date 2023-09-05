# wrapper for proxifyre

## Tested against Windows 10 / Python 3.10 / Anaconda and Ubuntu

## pip install proxifyapps

```python
app_infos = {
    "logLevel": "all",
    "proxies": [
        {
            "appNames": [r"C:\Program Files\Mozilla Firefox"],  # folder or name
            "socks5ProxyEndpoint": "127.0.0.1:1080",
            "username": None,
            "password": None,
            "supportedProtocols": ["UDP",'TCP'],
        },
        {
            "appNames": [r"Chrome"],  # folder or name
            "socks5ProxyEndpoint": "127.0.0.1:1081",
            "username": None,
            "password": None,
            "supportedProtocols": ["UDP",'TCP'],
        },
    ],
}
proxify_apps(app_infos, print_log=True)

# always use ctrl+c to kill the process
```