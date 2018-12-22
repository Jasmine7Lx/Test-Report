<template>
<div>
   <div class="d1">
      <!-- <span style="vertical-align: center">日期:</span> -->
      <el-date-picker
          v-model="select_date"
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
        v-model="select_text"
        >
      </el-input>
      </div>
      <div class="check">
        <el-button type="primary"  size="mini" round>
          搜索
        </el-button>
    </div>
    <div class="d3">
        <el-select v-model="select_show" placeholder="请选择">
          <el-option
            v-for="item in showlist"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
    </div>

</div>
</template>

<script>
  export default {
    data() {
      return {
        select_date: '',
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
        select_text: '',
        select_show: 'myself',
        showlist: [{
          value: 'myself',
          label: '只查看自己'
          }, {
            value: 'all',
            label: '查看全部'
          }, {
            value: 'pclist',
            label: '查看pc端报告'
          }, {
            value: 'phonelist',
            label: '查看移动端报告'
          }
        ]
      }
    }
  }
</script>

<style>
.d1,.d2{
  float: left;
  padding-left: 5px;
}
.d3 {
  float: right;
}
.check {
    display: inline-block;
    padding-left: 15px;
    padding-top: 5px;
}
</style>