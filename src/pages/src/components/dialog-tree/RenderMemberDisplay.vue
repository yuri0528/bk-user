<template>
  <div class="iam-member-display-wrapper">
    <label class="label">
      <i :class="[userIcon, 'icon']" />
      <span class="name">{{ title }}</span>
    </label>
    <div class="content">
      <div
        v-for="(item, index) in data"
        :key="index"
        class="member-item"
        :title="isDepartment ? (`${item.full_name}` ? `${item.full_name}` : ` ${item.name}`) :
          item.name !== '' ? `${item.username}(${item.email})` : item.username">
        <span v-if="isDepartment" class="member-name">
          {{ item.name ? item.name : item.full_name }}
        </span>
        <span v-else class="member-name">
          {{ item.username ? item.username : item.email }}
        </span>
        <template v-if="isDepartment && item.count">
          <span class="count">({{ item.count }})</span>
        </template>
        <template v-if="!isDepartment && item.email !== ''">
          <span class="display_name">({{ item.email }})</span>
        </template>
        <i class="user-icon icon-close-fill remove-icon" v-if="isEdit" @click="handleDelete(index)" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    data: {
      type: Array,
      default: () => [],
    },
    // user：用户，department：组织
    type: {
      type: String,
      default: 'user',
    },
    mode: {
      type: String,
      default: 'edit',
    },
  },
  computed: {
    userIcon() {
      return this.type === 'user' ? 'user-icon icon-personal-user' : 'user-icon icon-organization-fill';
    },
    title() {
      return this.type === 'user' ? this.$t('用户') : this.$t('组织');
    },
    isDepartment() {
      return this.type === 'department';
    },
    isEdit() {
      return this.mode === 'edit';
    },
  },
  methods: {
    handleDelete(payload) {
      this.$emit('on-delete', payload);
    },
  },
};
</script>
<style lang="postcss" scoped>
.iam-member-display-wrapper {
  margin-left: 10px;
  color: #63656e;
  .label {
    display: inline-block;
    margin-bottom: 9px;
    font-size: 12px;
    .icon {
      display: inline-block;
      color: #3a84ff;
      vertical-align: middle;
    }
    .name {
      display: inline-block;
      font-weight: 700;
      vertical-align: middle;
    }
  }
  .content {
    .member-item {
      position: relative;
      display: inline-block;
      margin: 0 6px 6px 0;
      padding: 0 10px;
      line-height: 22px;
      background: #f5f6fa;
      border: 1px solid #dcdee5;
      border-radius: 2px;
      font-size: 12px;
      &:hover {
        .remove-icon {
          display: block;
        }
      }
      .member-name {
        display: inline-block;
        max-width: 200px;
        line-height: 17px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: text-top;
        .count {
          color: #c4c6cc;
        }
      }
      .count,
      .display_name {
        display: inline-block;
        vertical-align: top;
      }
      .remove-icon {
        display: none;
        position: absolute;
        top: -6px;
        right: -6px;
        cursor: pointer;
      }
    }
  }
}
</style>
