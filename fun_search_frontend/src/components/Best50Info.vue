<template>
  <div class="best50_info">
    <h1>第</h1>
    <div id="select">
    <el-select v-model="value" placeholder="">
    <el-option
      id="option"
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
    </el-select>
    </div> 
    <h1>届金曲大赏</h1>
      </div>
</template>

<script>
export default {
  name: 'Best50Info',
  data() {
    return {
    options: [{
        value: '7th',
        label: '7'
    }, {
        value: '6th',
        label: '6'
    }, {
        value: '5th',
        label: '5'
    }, {
        value: '4th',
        label: '4'
    }, {
        value: '3rd',
        label: '3'
    }, {
        value: '2nd',
        label: '2'
    }, {
        value: '1st',
        label: '1'
    }],
    value: '7th'
    }
},
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
h1 {
  display: inline-block;
}
#select {
  display: inline-block;
  width: 7%
}
#option{
  display: block;
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
</style>