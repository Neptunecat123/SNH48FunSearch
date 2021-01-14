<template>
  <div class="members">
    <members-info />
    <member-info-table/>
  </div>
</template>

<script>
// @ is an alias to /src
import MembersInfo from '../components/MembersInfo.vue'
import MemberInfoTable from '../components/MemberInfoTable.vue'

export default {
  name: 'Members',
  components: {
    MembersInfo,
    MemberInfoTable,
  }
}
</script>
