<template>
  <div>
    <el-container style="display: flex; flex-direction: column; height: 100vh">
      <el-header class="header_container">
        <el-row>
          <el-col :span="6">
            <div class="left_header">
              租房信息可视化系统
            </div>
          </el-col>
          <el-col :span="13">
            <div class="right_header">
              <el-menu class="el-menu-demo" mode="horizontal" background-color="#C0C4CC" text-color="#fff"
                  active-text-color="#ffd04b">
                <el-menu-item class="menus_style" index="1">
                  <router-link style="color: blue;text-decoration: none" to="/home/data"><i class="el-icon-s-data"></i>数据展示</router-link>
                </el-menu-item>
                <el-menu-item class="menus_style" index="2">
                  <router-link style="color: blue;text-decoration: none" to="/home/average"><i class="el-icon-loading"></i>地区散点图</router-link>
                </el-menu-item>
                <el-menu-item class="menus_style" index="3">
                  <router-link style="color: blue;text-decoration: none" to="/home/pie"><i class="el-icon-pie-chart"></i>租金分析</router-link>
                </el-menu-item>
                <el-menu-item class="menus_style" index="4">
                  <router-link style="color: blue;text-decoration: none" to="/home/house"><i class="el-icon-office-building"></i>房源数量</router-link>
                </el-menu-item>
                <el-menu-item class="menus_style" index="5">
<!--                  <el-link type="primary" href="/home/averagerRent">平均房价</el-link>-->
                  <router-link style="color: blue;text-decoration: none" to="/home/averagerRent"><i class="el-icon-s-home"></i>平均房价</router-link>
                </el-menu-item>
                <el-menu-item class="menus_style" index="6">
                  <router-link style="color: blue;text-decoration: none" to="/home/map"><i class="el-icon-film"></i>地图展示</router-link>
                </el-menu-item>
              </el-menu>
            </div>
          </el-col>
          <el-col :span="2" class="avatar">
            <div>
              <el-avatar :src="require('@/assets/avatar.png')"></el-avatar>
            </div>
          </el-col>
          <el-col :span="1.5" class="elLogout">
            <div class="logoutButton">
              <el-button type="primary" plain @click="logout">退出</el-button>
            </div>
          </el-col>
          <el-col :span="1" class="elLogout">
            <div class="logsButton">
<!--              <el-button type="primary" plain @click="logsClick">日志</el-button>-->
              <el-dropdown>
                <el-button type="primary">
                  日志<i class="el-icon-arrow-down el-icon--right"></i>
                </el-button>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item>
                    <router-link style="color: blue;text-decoration: none" to="/home/admin">管理员</router-link>
                  </el-dropdown-item>
                  <el-dropdown-item>
                    <router-link style="color: blue;text-decoration: none" to="/home/data">黄金糕</router-link>
                  </el-dropdown-item>
                  <el-dropdown-item>
                    <router-link style="color: blue;text-decoration: none" to="/home/data">黄金糕</router-link>
                  </el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </div>
          </el-col>
        </el-row>
      </el-header>
      <el-main class="main">
        <router-view></router-view>
      </el-main>
<!--      <el-footer>Footer</el-footer>-->
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    logout () {
      window.sessionStorage.clear()
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped lang="less">
.main {
  height: 100%;
}
.header_container {
  height: 80px !important;
  background-color: #C0C4CC;
}
.left_header {
  display: flex;
  justify-content: center; /* 水平居中对齐 */
  align-items: center; /* 垂直居中对齐 */
  height: 80px; /* 可以根据需要调整容器的高度 */
  text-align: center; /* 水平文本居中对齐 */
  font-size: 34px;
  color: darksalmon;
}
.right_header {
  height: 80px;
  .el-menu-demo {
    height: 80px;
  }
}
.menus_style {
  display: flex;
  justify-content: center; /* 水平居中对齐 */
  align-items: center; /* 垂直居中对齐 */
  //height: 100px; /* 可以根据需要调整容器的高度 */
  text-align: center; /* 水平文本居中对齐 */
  height: 80px !important;
}
.avatar {
  margin-left: 50px;
  margin-top: 18px;
  width: 50px;
  display: flex;
  justify-content: center; /* 水平居中对齐 */
  align-items: center; /* 垂直居中对齐 */
}
.logoutButton {
  margin-top: 20px;
  margin-left: 25px;
}
.logsButton {
  margin-top: 20px;
  margin-left: 15px;
}
.elLogout {
  height: 80px !important;
  background-color: #C0C4CC;
}
</style>
