<template>
  <div>
    <el-menu :default-active="activeIndex" class="el-menu-demo" text-color="#000000" background-color="#B3C0D1" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">搜索</el-menu-item>
      <el-submenu index="2">
        <template slot="title">基本信息总览</template>
        <el-menu-item index="2-1">成员</el-menu-item>
        <el-menu-item index="2-2">Team</el-menu-item>
        <el-menu-item index="2-3">总选</el-menu-item>
        <el-menu-item index="2-3">B50</el-menu-item>
      </el-submenu>
      <el-menu-item index="3" disabled>随便看看</el-menu-item>
      <el-menu-item index="4">导入数据</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'nav',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.el-header {
    padding: 0; ;
    box-sizing: border-box;
    flex-shrink: 0;
}
</style>
