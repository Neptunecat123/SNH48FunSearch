<template>
    <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" @select="handleSelect" router>
      <el-menu-item index="/">首页</el-menu-item>
      <el-menu-item index="/members">成员信息</el-menu-item>
      <el-menu-item index="/election">总选数据</el-menu-item>
      <el-menu-item index="/best50">Best50</el-menu-item>
      <el-menu-item index="5" disabled>特殊公演</el-menu-item>
    </el-menu>
</template>

<script>
  export default {
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>