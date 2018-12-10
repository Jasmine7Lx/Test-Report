<template>
<div>
   <div class="d1">
      <!-- <span style="vertical-align: center">日期:</span> -->
      <el-date-picker
          v-model="value"
          type="daterange"
          align="right"
          unlink-panels
          range-separator="-"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          :picker-options="pickerOptions2"
          :default-time="['00:00:00', '23:59:59']">
      </el-date-picker>
   </div>
      <div class="d2">
      <el-input
        placeholder="请输入内容"
        prefix-icon="el-icon-search"
        >
      </el-input>
      </div>
      <div class="check">
        <el-button type="primary"  size="mini" round>
          搜索
        </el-button>
      </div>
</div>
</template>

<script>
  export default {
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
      }
    }
  }
</script>

<style>
.d1,.d2{
  float: left;
  padding-left: 5px;
}
.check {
    display: inline-block;
    padding-left: 15px;
    padding-top: 5px;
}
</style>