export const form1Rule = {
  rules: {
    demand_name: [{
      required: true,
      message: '请输入需求名称',
      trigger: 'blur'
    }],
    tester_name: [{
      required: true,
      message: '请输入测试人员',
      trigger: 'blur'
    }],
    developer_name: [{
      required: true,
      message: '请输入开发人员',
      trigger: 'blur'
    }],
    demander_name: [{
      required: true,
      message: '请输入产品负责人',
      trigger: 'blur'
    }],
  }
}
