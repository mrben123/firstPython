# 接口文档 同翔速检项目

## 接口名：/wordConvertData

## 附件1字段：

* 文件名：file_name
* 地区：city_and_area
* 乡镇：town
* 类型：industry
* 主治产品：main_product
* 产品：product
* 种植面积：area
* 产量：productivity

## 响应示例

```
[
    {
        'file_name':'乡镇分配试剂',
        'city_and_area':'泰安市泰山区',
        'town':'省庄镇',
        'industry':'种植业',
        'main_product':'主要治理产品',
	    'risk_points':'甲拌磷、三氯杀螨醇、氰戊菊酯',
        'product':'韭菜',
        'area':'8000',
        'productivity':'560',
    }，
    {
        'file_name':'乡镇分配试剂',
        'city_and_area':'泰安市泰山区',
        'town':'省庄镇',
        'industry':'水产业',
        'main_product':'主要治理产品',
	    'risk_points':'甲拌磷、三氯杀螨醇、氰戊菊酯',
        'product':'对虾',
        'area':'',
        'productivity':'560',
    }
]
```

## 附件2字段：

* 文件名：file_name
* 地区：city_and_area
* 乡镇：town
* 农业分管负责人：agriculture_owner
* 农业分管负责人姓名：agriculture_owner_name
* 农业分管负责人电话：agriculture_owner_tel
* 水产业分管负责人：aquatic_owner
* 水产业分管负责人姓名：aquatic_owner_name
* 水产业管分管负责人电话：aquatic_owner_tel
* 农业监管机构负责人：agriculture_mechanism
* 农业监管机构负责人姓名：agriculture_mechanism_name
* 农业监管机构负责人电话：agriculture_mechanism_tel
* 水产业监管机构负责人：aquatic_mechanism
* 水产业监管机构负责人姓名：aquatic_mechanism_name
* 水产业监管机构负责人电话：aquatic_mechanism_tel

## 响应示例

```
[
    {
        'file_name':'乡镇分配试剂',
        'city_and_area':'泰安市泰山区',
        'town':'省庄镇',
        'agriculture_owner':{
            'agriculture_owner_name':'张三',
            'agriculture_owner_tel':'16653853835',
            
        },
        'aquatic_owner':{
            'aquatic_owner_name':'张三',
            'aquatic_owner_tel':'16653853835'
        },
       
    }，
    {
        'file_name':'乡镇分配试剂',
        'city_and_area':'泰安市泰山区',
        'town':'省庄镇',
        'agriculture_mechanism':{
            'agriculture_mechanism_name':'张三',
            'agriculture_mechanism_tel':'16653853835'
        },
        'aquatic_mechanism':{
            'aquatic_mechanism_name':'张三',
            'aquatic_mechanism_tel':'16653853835'
        }
    }
]
```

## 附件3字段：

* 文件名：file_name
* 地区：city_and_area
* 单位：company
* 分管负责人：admin
* 分管负责人姓名：admin_name
* 分管负责人职务：admin_title
* 分管负责人办公电话：admin_tel
* 分管负责人手机：admin_mobile
* 具体工作负责人：staff
* 具体工作负责人姓名：staff_name
* 具体工作负责人职务：staff_title
* 具体工作负责人电话：staff_tel
* 具体工作负责人手机：staff_mobile

## 响应示例

```
[
    {
        'file_name':'乡镇分配试剂',
        'city_and_area':'泰安市',
        'company':'泰安市农业农村局',
        'admin':{
            'admin_name':'房振伟',
            'admin_title':'四级调研员',
            'admin_tel':'05387-6280056',
            'admin_mobile':'16653853835'
        }
    }，
    {
        'file_name':'乡镇分配试剂',
        'city_and_area':'泰安市',
        'company':'泰安市农业农村局',
        'staff':{
            'staff_name':'藏金波'，
            'staff_title':'农产品质量安全监管科科长',
            'staff_tel':'05387-6280056',
            'staff_mobile':'16653853835'
        }
        
    }
]
```