import {defineConfig} from '@playwright/test';
export default defineConfig({testDir:'./tests',testMatch:'**/*.spec.mjs',use:{baseURL:process.env.QA_BASE_URL||'http://127.0.0.1:5187',headless:true},workers:1,reporter:'list',webServer:process.env.QA_BASE_URL?undefined:{command:'npm run dev',url:'http://127.0.0.1:5187',reuseExistingServer:!process.env.CI,timeout:30000}});
