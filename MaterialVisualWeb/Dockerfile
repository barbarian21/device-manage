FROM harbor.uat.enflame.cc/enflame.cn/node:v16.7.0 AS builder

WORKDIR /workspace
COPY ./ ./

RUN npm install
RUN npm run build:prod

FROM harbor.uat.enflame.cc/library/nginx:1.19   
COPY --from=builder /workspace/dist/ /dist/

COPY ./default.conf /etc/nginx/conf.d/default.conf