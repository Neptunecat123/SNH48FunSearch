<template>
  <div class="election">
    <election-info />
    <election-info-table/>
  </div>
</template>

<script>
// @ is an alias to /src
import ElectionInfo from '../components/ElectionInfo.vue'
import ElectionInfoTable from '../components/ElectionInfoTable.vue'

export default {
  name: 'Election',
  components: {
    ElectionInfo,
    ElectionInfoTable,
  }
}
</script>