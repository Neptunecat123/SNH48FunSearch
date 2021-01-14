<template>
  <el-table
    :data="tableData"
    border
    style="width: 100%">
    <el-table-column
      prop="gname"
      label="团名"
      width="80">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="100">
    </el-table-column>
    <el-table-column
      prop="tname"
      label="队名"
      width="80">
    </el-table-column>
    <el-table-column
      prop="pname"
      label="期数"
      width="150">
    </el-table-column>
    <el-table-column
      prop="join_day"
      label="入团时间"
      width="120">
    </el-table-column>
    <el-table-column
      prop="birth_day"
      label="生日"
      width="120">
    </el-table-column>
    <el-table-column
      prop="birth_place"
      label="籍贯"
      width="100">
    </el-table-column>
    <el-table-column
      prop="ranking"
      label="总选名次"
      width="80">
    </el-table-column>
    <el-table-column
      prop="status"
      label="状态"
      width="80">
    </el-table-column>
    <el-table-column
      prop="catch_phrase"
      label="CatchPhrase">
    </el-table-column>
  </el-table>
</template>

<script>
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄'
        }, {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄'
        }]
      }
    }
  }
</script>