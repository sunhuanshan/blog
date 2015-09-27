/**
  * author sunhuanshan
  * date 2015-09025
 **/
$(document).ready(function() {
    function render(param, url, ele) {
        $.getJSON(url, param, function (resp) {
            if (resp.success) {
                ele.html('').html(resp.html);
            } else {
                alert(resp.detail);
            }
        })
    }

    $('.end').click(function () {
        var page_id = $(this).attr('page_id');
        var param = {"id": page_id};
        var url = "/page";
        var ele = $('#articles');
        render(param, url, ele);
    });

    $('#input_area').focus(function(){
       if($(this).val() == '说点什么...') {
           $(this).val('');
       }
    });

    var review_box = $('#review_box');
    $('.input-review .commit-btn').click(function(){
        if($('#input_area').val()=='' || $('#input_area').val()=='说点什么...') {
            alert('请输入评论');
            return;
        }
        review_box.removeClass('hide');
    });

    review_box.find('.close').click(function(){
        review_box.addClass('hide');
    });

    review_box.find('.is_visitor').click(function(){
        if ($(this).attr('checked') == 'checked') {
            $(this).removeAttr('checked');
        } else {
            $(this).attr('checked', true);
        }
    });

    review_box.find('.submit-btn').click(function(){
        var at_id = $('#single_article').attr('article_id');
        var comment = $('#input_area').val();
        comment = comment.replace(/@[0-9a-zA-Z\u4E00-\u9FA5]+:/, '');
        var email = review_box.find(".email").val();
        var name = review_box.find(".name").val();
        var is_visitor = review_box.find('.is_visitor').attr('checked');
        var answer = '';
        if ($('#input_area').data('answer')) {
            var answer = $('#input_area').data('answer');
        }
        var param = {'id':at_id, 'comment':comment, 'answer' :answer};
        if(is_visitor) {
            param['is_visitor']=is_visitor;
        } else {
            if(email == '' || name == '') {
                alert('邮箱和名字不可以为空');
                return;
            }
            param['email'] = email;
            param['name'] = name;
        }
        var url='/addReview';
        $.getJSON(url, param, function(resp){
            if(resp.success) {
               $('.review-history').html('').html(resp.html);
               review_box.addClass('hide');
               if(review_box.find('.is_visitor').attr('checked') == 'checked') {
                   review_box.find('.is_visitor').removeAttr('checked');
               }
               review_box.find("email").val('');
               review_box.find("name").val('');
               $('#input_area').val('说点什么...');
            } else {
                alert('评论失败');
            }
        })
    });
    var input_review = $('#input_area');
    $('body').on('click', '.single-review .replay', function(){
        var reviewer = $(this).parent().parent().find('.reviewer').text();
        input_review.val('@' + reviewer + ':');
        input_review.data('answer', reviewer)
        input_review.focus();
    });
});