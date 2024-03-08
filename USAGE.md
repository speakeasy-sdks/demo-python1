<!-- Start SDK Example Usage [usage] -->
```python
import dataservice
from dataservice.models import components

s = dataservice.Dataservice(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = components.LogRequest(
    dataset_id='<value>',
    multiple=components.LogMultiple(
        columns=[
            '<value>',
        ],
        data=[
            [
                [
                    2469.2,
                ],
            ],
        ],
    ),
)

res = s.profile.log(req)

if res.any is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->