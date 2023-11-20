<template>
  <div class="china-map-container">
    <div ref="chinaMap" style="width: 100%; height: 500px;"></div>
  </div>
</template>

<script>
import echarts from 'echarts'
// import china from 'echarts/asset/china.json'

export default {
  name: 'leftCard',
  data () {
    return {
      myChart: null,
      mapData: [
        {
          name: "南海诸岛",
          value: 100,
          eventTotal: 100,
          specialImportant: 10,
          import: 10,
          compare: 10,
          common: 40,
          specail: 20
        },
        {name: "北京", value: 540},
        {name: "天津", value: 130},
        {name: "上海", value: 400},
        {name: "重庆", value: 750},
        {name: "河北", value: 130},
        {name: "河南", value: 830},
        {name: "云南", value: 110},
        {name: "辽宁", value: 19},
        {name: "黑龙江", value: 150},
        {name: "湖南", value: 690},
        {name: "安徽", value: 60},
        {name: "山东", value: 39},
        {name: "新疆", value: 452},
        {name: "江苏", value: 31},
        {name: "浙江", value: 104},
        {name: "江西", value: 36},
        {name: "湖北", value: 52},
        {name: "广西", value: 33},
        {name: "甘肃", value: 73},
        {name: "山西", value: 54},
        {name: "内蒙古", value: 778},
        {name: "陕西", value: 22},
        {name: "吉林", value: 44},
        {name: "福建", value: 18},
        {name: "贵州", value: 54},
        {name: "广东", value: 98},
        {name: "青海", value: 13},
        {name: "西藏", value: 0},
        {name: "四川", value: 44},
        {name: "宁夏", value: 42},
        {name: "海南", value: 22},
        {name: "台湾", value: 23},
        {name: "香港", value: 25},
        {name: "澳门", value: 555}
      ]
    }
  },
  mounted() {
    this.initChinaMap();
  },
  methods: {
    async initChinaMap() {
      const response = await fetch("require('@echarts/asset/china.json')"); // 替换为你的中国地图数据文件的路径
      console.log(response)
      const chinaMapData = await response.json();
      console.log(chinaMapData)

      echarts.registerMap('china', chinaMapData); // 注册中国地图数据

      const myChart = echarts.init(this.$refs.chinaMap);

      const option = {
        tooltip: {
          trigger: 'item',
          formatter: '{b}: {c} (人)'
        },
        visualMap: {
          min: 0,
          max: 500,
          left: 'left',
          top: 'bottom',
          text: ['高', '低'],
          calculable: true
        },
        series: [
          {
            name: '人口数量',
            type: 'map',
            mapType: 'china',
            roam: false,
            label: {
              show: true
            },
            data: this.mapData,
          },
        ],
      };

      myChart.setOption(option);
    },
  },
};
</script>

<style>
.china-map-container {
  width: 100%;
  height: 500px;
}
</style>
