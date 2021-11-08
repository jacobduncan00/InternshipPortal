<template>
  <div>
    <Navbar />
    <Notifications />
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import Notifications from "../../components/Notifications.vue";
export default {
  name: "NotificationPage",
  components: {
    Navbar,
    Notifications,
  },
};
</script>
