#!/bin/bash

echo "创建role"
:<<!
echo "role"

python manager.py cms_role_add -n "InactiveUser" -d "未激活用户"
python manager.py cms_role_add -n "RegularUser" -d "普通会员"
python manager.py cms_role_add -n "UserLevel_1" -d "一级会员"
python manager.py cms_role_add -n "UserLever_2" -d "二级会员"
python manager.py cms_role_add -n "Administrator" -d "管理员"
python manager.py cms_role_add -n "SuperAdmin"   -d "超级管理员"

echo "创建用户角色表"

python manager.py cms_role_user_add -u 1 -r 2


echo "添加资源"
python manager.py cms_resource_add -n "修改用户名" -u "/api/v1/userUpdateUsername/"



echo "添加角色资源表"
python manager.py cms_resource_role_add -r 2 -s 1

!
echo "删除用户某个角色"
python manager.py cms_role_user_del -u 1 -r 2