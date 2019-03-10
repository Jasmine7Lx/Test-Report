<template>
<div>
  <div :class="className" :id="id" :style="{height:height,width:width}" ref="myEchart">
  </div>
  <h1>{{bugList}}</h1>
</div>
</template>
<script>
import echarts from 'echarts'
import https from '../https.js'
export default {
  props: {
    className: {
      type: String,
      default: 'yourClassName'
    },
    id: {
      type: String,
      default: 'yourID'
    },
    width: {
      type: String,
      default: '1000px'
    },
    height: {
      type: String,
      default: '500px'
    }
  },
  data() {
    return {
      chart: null,
      bugList: []
    }
  },
  mounted() {
    this.initChart();
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$refs.myEchart);
      // 把配置和数据放这里
      this.chart.setOption({
        color: ['#3398DB'],
        tooltip: {
          trigger: 'axis',
          axisPointer: { // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '2%',
          bottom: '13%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          data: ['视频播放', '音乐播放', '信息流', '手游', '登录', '三国', '设置'],
          axisTick: {
            alignWithLabel: true
          }
        }],
        yAxis: [{
          type: 'value'
        }],
        series: [{
          name: 'bug数量',
          type: 'bar',
          barWidth: '60%',
          data: [7, 5, 2, 0, 10, 3, 1]
        }]
      })
    },
    getBugs: function() {
        https.fetchGet('/api/buglist')
        .then((resp) => {
            console.log(resp)
            this.bugList = resp.data.data;
        })
    },
  },
  created() {
    this.getBugs()
  },
}
</script>
