<template>
  <div class="edit">
    <span>需求为：{{report.demand_name}}，测试结果如下:</span>
    <el-form label-position="left" label-width="180px">
      <el-form-item label="一、测试结论：">{{report.result | resWord }}</el-form-item>
      <el-form-item label="二、遗留问题：">
        <p v-for="(item,index) in remain" :key="index" >
          {{item.remain__content}}
        </p>
      </el-form-item>
      <el-form-item label="三、测试说明：">
        <br>
        <el-form>
          <el-form-item label="1.测试环境：">{{report.env | envWord}}</el-form-item>
          <el-form-item label="2.环境配置：">
            <p v-for="(item,index) in config" :key="index">{{item.config__content}}</p>
          </el-form-item>
          <el-form-item label="3.测试版本/链接：">
            <p v-for="(item,index) in build" :key="index">{{item.build__site}}</p>
          </el-form-item>
          <el-form-item label="4.测试时间：">
            <el-date-picker
              v-model="testTime"
              readonly
              type="datetimerange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
            ></el-date-picker>
          </el-form-item>
        </el-form>
      </el-form-item>
      <el-form-item label="四、测试中发现的问题：">
        <br>
        <el-form label-position="left" label-width="100px">
          <el-form-item label="1.前端bug：">
            <p v-for="(item,index) in frontBug" :key="index">
              <span>{{item.bug__content}}</span>
              <el-tag v-if="item.bug__status=='solve'" type="success">已解决</el-tag>
              <el-tag v-if="item.bug__status=='no_solve'" type="danger">待解决</el-tag>
              <el-tag v-if="item.bug__status=='noneed_solve'" type="info">无需解决</el-tag>
            </p>
          </el-form-item>
          <el-form-item label="2.后端bug：">
            <p v-for="(item,index) in backBug" :key="index">
              <span>{{item.bug__content}}</span>
              <el-tag v-if="item.bug__status=='solve'" type="success">已解决</el-tag>
              <el-tag v-if="item.bug__status=='no_solve'" type="danger">待解决</el-tag>
              <el-tag v-if="item.bug__status=='noneed_solve'" type="info">无需解决</el-tag>
            </p>
          </el-form-item>
        </el-form>
      </el-form-item>
      <el-form-item label="五、兼容性：">
        <br>
        <el-form label-position="left" label-width="100px">
          <el-form-item label="1.电脑系统：">
            <p v-for="(item,index) in computer" :key="index">{{item.system}}</p>
          </el-form-item>
          <el-form-item label="2.浏览器：">
            <p v-for="(item,index) in browser" :key="index">{{item.system}}</p>
          </el-form-item>
        </el-form>
      </el-form-item>
    </el-form>
    <!-- <span style="font-size:16.5px; padding-left:10px;">六、测试用例：</span>
    <span class="explain">链接：</span>
    <span class="explain">文件：</span> -->
  </div>
</template>
<script>
import https from "../https.js";
// import Mock from "@/constants/mock";
export default {
  filters: {
    resWord(res) {
      if (res == "pass") {
        return "测试通过";
      }
      else if(res == "block"){
        return "测试不通过"
      }
      else if(res == "finish"){
        return "测试完成"
      }
    },
    envWord(env) {
      if (env == "test") {
        return "测试环境";
      }
      else if(env == "formal"){
        return "正式环境"
      }
      else if(env == "gray"){
        return "灰度环境"
      }
    }
  },
  data() {
    return {
      remain: [],
      report: [],
      config: [],
      build: [],
      bug: [],
      compat: []
    };
  },
  computed: {
    testTime() {
      return [this.report.start_time, this.report.end_time];
    },
    frontBug() {
      return this.bug.filter(ele => {
        return ele.bug__bug_type == "frontbug";
      });
    },
    backBug() {
      return this.bug.filter(ele => {
        return ele.bug__bug_type == "backbug";
      });
    },
    computer() {
      return this.compat.filter(ele => {
        return ele.compat_type == "computer";
      });
    },
    browser() {
      return this.compat.filter(ele => {
        return ele.compat_type == "browser";
      });
    }
  },
  methods: {
    formatDate: function(row, column) {
      const date = row[column.property];
      if (date === undefined) {
        return "";
      }
      //这里的格式根据需求修改
      return moment(date).format("YYYY-MM-DD");
    },
    getReportDetail: function() {
      // this.remain = Mock.remain;
      // this.report = Mock.report[0];
      // this.config = Mock.config;
      // this.build = Mock.build;
      // this.bug = Mock.bug;
      // this.compat = Mock.compat;
      let reportId = this.$route.params.id;
      https.fetchGet('api/pcreport', {id:reportId})
        .then((resp) => {
            // console.log(resp.data.data);
            this.remain = resp.data.data.remain;
            this.report = resp.data.data.report[0];
            this.config = resp.data.data.config;
            this.build = resp.data.data.build;
            this.bug = resp.data.data.bug;
            this.compat = resp.data.data.compat;
        })
    }
  },
  created() {
    this.getReportDetail();
  }
};
</script>

<style>
p {
  margin: 0;
}
</style>

