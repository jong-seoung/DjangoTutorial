from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from bbs.models import Article
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# 게시글 목록
class ArticleListView(TemplateView):
    template_name = 'base.html'
    queryset = Article.objects.all()         # 모든 게시글

    def get(self, request, *args, **kwargs):

        # 템플릿에 전달할 데이터
        ctx = {
            'view': self.__class__.__name__, # 클래스의 이름
            'data': self.queryset            # 검색 결과
        }
        return self.render_to_response(ctx)

# 게시글 상세
class ArticleDetailView(TemplateView):
    template_name = 'base.html'
    queryset = Article.objects.all()
    pk_url_kwargs = 'article_id'                 # 검색데이터의 primary key를 전달받을 이름

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset     # queryset 파라미터 초기화
        pk = self.kwargs.get(self.pk_url_kwargs) # pk는 모델에서 정의된 pk값, 즉 모델의 id
        return queryset.filter(pk=pk).first()    # pk로 검색된 데이터가 있다면 그 중 첫번째 데이터 없다면 None 반환

    def get(self, request, *args, **kwargs):
        article = self.get_object()
        if not article:
            raise Http404('invalid article_id')  # 검색된 데이터가 없다면 에러 발생

        ctx = {
            'view': self.__class__.__name__,
            'data': article
        }
        return self.render_to_response(ctx)

# 게시글 추가, 수정
@method_decorator(csrf_exempt, name='dispatch')   # 모든 핸들러 예외 처리
class ArticleCreateUpdateView(TemplateView):
    template_name = 'base.html'
    queryset = Article.objects.all()
    pk_url_kwargs = 'article_id'
    
    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        article = queryset.filter(pk=pk).first()
        
        if pk and not article:                    # 검색결과가 없으면 곧바로 에러 발생
            raise Http404('invalid pk')
        return article

    def get(self, request, *args, **kwargs):
        article = self.get_object()

        ctx = {
            'view': self.__class__.__name__,
            'data': article
        }
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        post_data = {key: request.POST.get(key) for key in ('title', 'content', 'author')}
        for key in post_data:
            if not post_data[key]:
                raise Http404('no data for {}'.format(key))

        if action == 'create':
            article = Article.objects.create(title=title, content=content, author=author)
        elif action == 'update':
            article = self.get_object()
            for key, value in post_data.items():
                setattr(article, key, value)
            article.save()
        else:
            raise Http404('invalid action')

        ctx = {
            'view': self.__class__.__name__,
            'data': article
        }
        return self.render_to_response(ctx)
        
def hello(request, to):
    return HttpResponse('Hello {}.'.format(to))
