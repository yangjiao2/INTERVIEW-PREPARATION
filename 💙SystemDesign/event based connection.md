[Long polling, WebSockets, Server-Sent Events (SSE))](https://dev.to/karanpratapsingh/system-design-long-polling-websockets-server-sent-events-sse-1hip)

## Summary

| Category |  Advantage | Cons | Senarios |
| -- |---| ----- | -------- |
| Long polling |
| WebSockets | 1)  real-time bidirectional communication 2) remove redundant 'XMLHttpRequest’ headers | since use TCP (custom protocol) instead of HTTP, 1) no compression 2) no multiplexing |  real-time polling, chat, media players, multiplayer games |
| Server-Sent Events (SSE) | 1) transport messages over HTTP 2) built-in connection support for reconnection  | 1) restrictinons the maximum open connections which not favor for multi tabs | status updates, social-media news feeds, push notifications, newsletters, live stock or news tickers |
| HTTP streaming |

![](pics/sse.jpeg)

## Techinique

### HTTP long polling (***half-duplex***): The server holds a client connection open to deliver a response when new data becomes available or the connection timeout threshold is reached.

1) longer timeout period (via a Keep-Alive header) when listening for a response

2) leaving an HTTP connection open:

 -> server can continue to deliver response data for as long as the connection remains open

 -> client could keeps sending request data

---

### WebSocket (***two-way, full-duplex***): Provides ***two-way, full-duplex*** communication channels over a ***persistent TCP connection***, with much ***lower overhead*** than half-duplex alternatives such as HTTP long polling.

1) on top of TCP/IP stack: change on handshake and header structure

2) multiple subprotocols: JSON, XML, MQTT, WAMP.

3) after handshake, client sent request for upgrade to Websocket
```
GET /index.html HTTP/1.1
Host: www.example.com
Connection: Upgrade
Upgrade: websocket
```

4) security: `Sec-WebSocket-Key` and `Sec-WebSocket-Accept` attached on request


![websockets.webp](pics/websockets.webp)

---

### MQTT: publish-subscribe messaging protoco for streaming data between devices with limited CPU power and/or battery life, such as IoT devices; built on the TCP/IP protocol


---

### SSE: lightweight, subscribe-only protocol for event-driven data streams.

employ a JavaScript API called **EventSource** to register with the event source and transmit messages or continuous updates to a client.
