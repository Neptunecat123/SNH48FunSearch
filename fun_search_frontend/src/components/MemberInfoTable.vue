<template>
  <div>
  <div>
  <el-table
    :data=info
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
  </div>
  <div>
  <el-pagination
  background
  layout="prev, pager, next"
  :current-page.sync="currentPage"
  :total="totalPage"
  @current-change="handleCurrentChange">
</el-pagination>
  </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        info: [],
        currentPage: 1,
        totalPage: 0,
        loaded: false
      }
    },
    methods: {
      getData(currentPage){
        this.info = []
        axios.get('http://127.0.0.1:5000/membertable', {
            params: {
              page: currentPage,
            }
          })
          .then(response => (console.log(response.data.total_page), this.info = response.data.data, this.totalPage = response.data.total_page, this.loaded = true))
      },
      handleCurrentChange(val) {
        this.currentPage = val
        this.getData(this.currentPage)
      }
    },
    mounted () {
      this.getData(1)
    },
  }
</script>