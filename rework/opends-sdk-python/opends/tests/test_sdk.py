#!/usr/bin/env python
# -*- coding: utf-8 -*-
from opends.sdk import BDPClient
from opends.sdk import DS

ACCESS_TOKEN = "1aed84f0292c86010fc742fab90e7c44"  #这里需要填写自己的token
DOMAIN = "haizhi"  # 这里更换为自己的企业域

ds_name = u"your_ds_name"
table_name = u"your_table_name"
table_name_alias = u"table_alias"

client = BDPClient(ACCESS_TOKEN, "haizhi")
all_ds = client.get_all_ds()
# client.delete_ds(ds_name)
# ds = client.create_ds(ds_name)  # type:DS
ds = client.get_ds(ds_name)    # type:DS

ds.get_all_tables()
# ds.delete_table(table_name)


# 工作表操作
def create_table():
    schema = [
        {
            "remark": "",
            "name": "id",
            "type": "number",
            "title": "ident"
        },
        {
            "remark": "",
            "name": "name",
            "type": "string"
        },
        {
            "remark": "",
            "name": "height",
            "type": "number"
        },
        {
            "remark": "",
            "name": "join_time",
            "type": "date"
        },
        {
            "remark": "",
            "name": "mark",
            "type": "string",
            "title": "words"
        }
    ]
    return ds.create_table(table_name, schema=schema, uniq_key=["id"], title=table_name_alias)

table = create_table()
table = ds.get_table(table_name)

fields = ["id", "name", "age"]
data = [[1, "user1", 13], [2, "user2", 14]]
table.insert_data_by_name(fields, data)
table.commit()


# 字段操作
table.get_fields()
field_name = "field_name"
table.add_field("field_name", "string", 0, "alias_field")

table.delete_field(field_name)
table.preview()
