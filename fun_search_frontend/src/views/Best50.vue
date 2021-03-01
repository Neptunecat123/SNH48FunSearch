<template>
  <div class="best50">
    <best-50-info/>
    <best-50-table/>
  </div>
</template>

<script>
// @ is an alias to /src
import Best50Info from '../components/Best50Info.vue'
import Best50Table from '../components/Best50Table.vue'

export default {
  name: 'Best50',
  components: {
    Best50Info,
    Best50Table,
  }
}
</script>