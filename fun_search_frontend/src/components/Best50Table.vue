<template>
  <div>
  <div>
  <el-table
    :data=info
    @filter-change="handleFilterChange"
    border
    style="width: 100%">
    <div v-if="time!=7">
    <el-table-column
      prop="group"
      column-key="group"
      label="组"
      width="100"
      >
    </el-table-column>
    </div>
    <el-table-column
      prop="rank"
      column-key="rank"
      label="排名"
      width="100"
      >
    </el-table-column>
    <el-table-column
      prop="unit"
      column-key="unit"
      label="曲目"
      width="150">
    </el-table-column>
    <el-table-column
      prop="unit_from"
      column-key="unit_from"
      label="来源"
      width="150">
    </el-table-column>
    <el-table-column
      prop="number"
      column-key="number"
      label="人数"
      width="100">
    </el-table-column>
    <el-table-column
      prop="members"
      label="表演人员">
    </el-table-column>
  </el-table>
  </div>
  <div>
  </div>
  </div>
   </template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        info: [],
        time: 7

      }
    },
    methods: {
      getData(){
        this.info = []
        axios.get('http://127.0.0.1:5000/b50table', {
            params: {
              time: this.time,
            }
          })
          .then(response => (console.log(response.data), this.info = response.data))
      },
    },
    mounted () {
      this.getData()
    },
  }
</script>