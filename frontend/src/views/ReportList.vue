<template>
<div>
   <div>
        <select-list></select-list>
   </div>
   <div>
        <show-list></show-list>
   </div>
</div>
</template>

<script>
  import SelectList from '@/components/ReportList/SelectList'
  import ShowList from '@/components/ReportList/ShowList'
  export default {
    components: {
      'selectList': SelectList,
      'showList': ShowList,
    },
  }
</script>

<style>

</style>
