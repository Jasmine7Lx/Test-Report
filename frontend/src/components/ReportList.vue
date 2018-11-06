<template>
<div>
   <div>
      <!-- <span style="vertical-align: center">日期:</span> -->
      <el-date-picker
          v-model="value"
          type="daterange"
          align="right"
          unlink-panels
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          :picker-options="pickerOptions2"
          :default-time="['00:00:00', '23:59:59']">
      </el-date-picker>
      <div class="test">
        <el-button type="primary" icon="el-icon-search" size="mini" round>
          搜索
        </el-button>
      </div>
   </div>
   <show-list></show-list>
</div>
</template>

<script>
  import ShowList from './ShowList'
  export default {
    components: {
      'showList': ShowList,
    },
    data() {
      return {
        pickerOptions2: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        value: ''
      };
    }
  }
</script>

<style>
.test {
    display: inline-block;
    padding-left: 15px;
}
.el-table-column {
  background-color: midnightblue
}
</style>
