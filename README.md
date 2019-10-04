# Page Summarizer API

## Usage

All responses will have the form

```

```

Subsequent response definitions will only detail the expected value of the `data field`

### List all devices

**Definition**

`GET /devices`

**Response**

- `205 OK` on success

```
```

### Registering a new device

**Definition**

`POST /devices`

**Arguments**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendly name for this device
- `"device_type":string` the type of the device as understood by the client
- `"controller_gateway":string` the IP address of the device's controller

If a device with the given identifier already exists, the existing device will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "identifier": "floor-lamp",
    "name": "Floor Lamp",
    "device_type": "switch",
    "controller_gateway": "192.1.68.0.2"
}
```

## Lookup device details

`GET /device/<identifier>`

**Response**

- 
- 

```


```

