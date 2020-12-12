<template>
  <div>
    <el-container>
        <el-header><Navbar></Navbar></el-header>
      
      <el-main>
        <div class="img_fun">
          <img alt="Vue logo" src="../assets/2.png">
        </div>
        <div class="input">
          <el-input style="width: 60%" v-model="input" placeholder="请输入内容"></el-input>
        </div>
        <div class="search_btn">
          <el-button type="primary">查！</el-button>
        </div>
      </el-main>
      <el-footer>
        <Footer></Footer>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import Navbar from '../common/nav.vue'
import Footer from '../common/footer.vue'

export default {
  name: 'index',
  components: {
    Navbar,
    Footer
  },
  props: {
    msg: String
  },
  data() {
      return {
        activeIndex: '1',
        activeIndex2: '1',
        input: ''
      };
    },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

.el-header, .el-footer {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 90px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}

</style>
