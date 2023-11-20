<template>
  <div>
    <div class="dataPresentation">
      <h1>
        数据展示
      </h1>
    </div>
<!--    数据上方选择栏   -->
    <div>
      <el-row>
      <el-col :span="4">
        <div class="grid-content bg-purple">
          <el-select v-model="selectedProvince" @change="loadCities" placeholder="请选择省份">
<!--            <el-option value="请选择省份">请选择省份</el-option>-->
            <el-option v-for="province in provinces" :key="province" :value="province">
            </el-option>
          </el-select>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple-light">
          <el-select v-model="selectedCity" @change="loadCitiesDowntown" placeholder="请选择市区">
<!--            <el-option value="请选择市区">请选择市级</el-option>-->
            <el-option v-for="city in cities" :key="city" :value="city">
            </el-option>
          </el-select>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple-light">
          <el-select v-model="selectedDowntown" placeholder="请选择县级">
<!--            <el-option value="请选择市区">请选择县级</el-option>-->
            <el-option v-for="downtown in downtowns" :key="downtown" :value="downtown">
            </el-option>
          </el-select>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="grid-content bg-purple">
          <el-button type="primary" @click="searchData">搜索</el-button>
        </div>
      </el-col>
    </el-row>
    </div>
<!--    表格数据    -->
    <el-table :data="dataList" style="width: 100%">
      <el-table-column prop="province" label="省份" width="80"></el-table-column>
      <el-table-column prop="city" label="市级" width="100"></el-table-column>
      <el-table-column prop="downtown" label="县级" width="80"></el-table-column>
      <el-table-column prop="introduce" label="介绍" width="300"></el-table-column>
      <el-table-column prop="address" label="详细地址" width="300"></el-table-column>
      <el-table-column prop="area" label="房屋面积" width="120"></el-table-column>
      <el-table-column prop="orientation" label="朝向" width="120"></el-table-column>
      <el-table-column prop="pattern" label="格局" width="120"></el-table-column>
      <el-table-column prop="rent" label="每月租金" width="120"></el-table-column>
      <el-table-column prop="link" label="链接">
        <template slot-scope="scope">
          <el-link :href="scope.row.link" target="_blank" type="primary">详情页</el-link>
        </template>
      </el-table-column>
    </el-table>
    <div>
      <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="queryInfo.page_num"
      :page-sizes="[8, 20, 50, 100]"
      :page-size="queryInfo.page_size"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total">
    </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Data',
  created () {
    this.getDataList()
    this.getProvinceList()
  },
  data () {
    return {
      queryInfo: {
        province: '',
        city: '',
        downtown: '',
        page_num: 1,
        page_size: 8
      },
      dataList: [],
      total: 0,
      selectedProvince: '',
      selectedCity: '',
      selectedDowntown: '',
      provinces: [],
      cities: [],
      downtowns: []
    }
  },
  methods: {
    async getDataList () {
      const { data: res } = await this.$axios.get('/user/user', { params: this.queryInfo })
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.dataList = res.data.data_list
      this.total = res.data.totalPage
    },
    handleSizeChange (val) {
      this.queryInfo.page_size = val
      this.getDataList()
    },
    handleCurrentChange (val) {
      this.queryInfo.page_num = val
      this.getDataList()
    },
    async getProvinceList () {
      this.queryInfo.province = this.selectedProvince
      this.queryInfo.province = this.selectedCity
      const { data: res } = await this.$axios.get('/home/data/province_list', { params: this.queryInfo })
      // console.log(res)
      this.provinces = res.data || []
    },
    async loadCities () {
      this.selectedCity = ''
      this.selectedDowntown = ''
      this.queryInfo.province = this.selectedProvince
      const { data: res } = await this.$axios.get('/home/data/city_list', { params: this.queryInfo })
      console.log(res)
      this.cities = res.data || []
    },
    async loadCitiesDowntown () {
      this.selectedDowntown = ''
      this.queryInfo.province = this.selectedProvince
      this.queryInfo.city = this.selectedCity
      const { data: res } = await this.$axios.get('/home/data/downtown_list', { params: this.queryInfo })
      console.log(res.data)
      this.downtowns = res.data || []
    },
    async searchData () {
      this.queryInfo.province = this.selectedProvince
      this.queryInfo.city = this.selectedCity
      this.queryInfo.downtown = this.selectedDowntown
      const { data: res } = await this.$axios.get('/user/user', { params: this.queryInfo })
      if (res.status !== 200) return this.$msg.error(res.msg)
      this.getDataList()
    }
  }
}
</script>

<style scoped lang="less">
.dataPresentation {
    display: flex;
    justify-content: center; /* 水平居中对齐 */
    align-items: center; /* 垂直居中对齐 */
    //height: 100px; /* 可以根据需要调整容器的高度 */
    text-align: center; /* 水平文本居中对齐 */
    height: 80px !important;
}
</style>
