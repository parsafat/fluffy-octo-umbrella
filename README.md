# Stampede

Stampede is a Telegram bot for dealing with user management on [Xray](https://github.com/XTLS/Xray-core/).

![demo](demo.gif)

## Features

- Users with custom usernames (emails) can be added
- Users can be either persistent (surviving Xray restarts) or non-persistent
- A URI and QR code are provided for user connection upon creation
- A list of users is available
- Traffic usage for each user since the last Xray restart can be monitored
- Users can be removed as needed

## Known Limits

- Only VLESS inbounds are supported

## Configuration Guide

This section provides details on how to configure the `config.ini` file. The configuration file is organized into three sections: `[telegram]`, `[xray]`, and `[uri]`. Below are the explanations for each section.

### [telegram] Section

This section configures your Telegram bot. The `bot_token` is required for the bot to function and can be obtained from [BotFather](https://t.me/BotFather). The `super_user_id` should be set to the Telegram user ID of the individual who will have administrative control over the bot.

### [xray] Section

This section configures Xray, including its API and statistics features. The `config` entry specifies the path to your Xray configuration file. The `api_address` is the address on which the Xray API listens, and the `api_port` is the port number for the API. These values should match those specified in your Xray configuration file.

#### Xray Configuration Notes

Ensure that the Xray API is configured to enable `HandlerService` and `StatsService` in the [API settings](https://xtls.github.io/config/api.html#apiobject) of your Xray configuration. Also, include the [`stats` object](https://xtls.github.io/config/stats.html#statsobject) and configure the [policy settings](https://xtls.github.io/config/policy.html#policyobject) to track relevant data.

For detailed configuration instructions on statistics, refer to the [V2Fly Traffic Statistics Tutorial](https://guide.v2fly.org/advanced/traffic.html). As mentioned earlier, also ensure that `HandlerService` is enabled for adding and removing users. If using Xray version 1.8.13 or later, you can simplify the configuration by utilizing the `listen` item in the `api` object instead of adding a `dokodemo-door` inbound.

Also, to ensure proper functionality of this bot, the main inbound object that contains the users must have the tag 'vless'.

### [uri] Section

This section defines the connection details for your users. The `address` is the address of the proxy server, `port` is the port on which the proxy server operates, and `path` is the path used to connect to the server.

## Installation

Before running the bot, make sure you install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
./stampede.py
```
